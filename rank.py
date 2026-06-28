import gzip
import json
import argparse
import csv
TARGET_TITLES = {"ai engineer", "ml engineer", "machine learning engineer", "data scientist"}
TARGET_SKILLS = {"embeddings", "retrieval", "ranking", "vector database", "python", "nlp"}
def calculate_match_score(candidate):
    """
    Computes a quick local score based on title and skill overlap.
    Avoids heavy LLM calls to stay within the 5-minute runtime limit.
    """
    score = 0.0
    profile = candidate.get("profile", {})
    skills_list = candidate.get("skills", [])
    current_title = profile.get("current_title", "").lower()
    for title in TARGET_TITLES:
        if title in current_title:
            score += 0.5
            break
    matched_skills = 0
    for skill in skills_list:
        skill_name = skill.get("name", "").lower()
        if any(target in skill_name for target in TARGET_SKILLS):
            matched_skills += 1
    score += min(matched_skills * 0.1, 0.5)
    reasoning = f"{profile.get('current_title', 'Engineer')} matching {matched_skills} core JD skills."
    return score, reasoning
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", default="./candidates.jsonl.gz", help="Path to candidates pool")
    parser.add_argument("--out", default="./sample_submission.csv", help="Output file name verbatim")
    args = parser.parse_args()
    ranked_candidates = []
    print("Processing 100,000 candidates...")
    with gzip.open(args.candidates, "rt", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            candidate = json.loads(line)
            cid = candidate["candidate_id"]
            score, reasoning = calculate_match_score(candidate)
            ranked_candidates.append((cid, score, reasoning))
    ranked_candidates.sort(key=lambda x: (-x[1], x[0]))
    print("Writing top 100 entries to CSV...")
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["candidate_id", "rank", "score", "reasoning"])
        for i, (cid, score, reasoning) in enumerate(ranked_candidates[:100], start=1):
            writer.writerow([cid, i, round(score, 4), reasoning])
    print(f"Task I complete! Output saved to {args.out}")
if __name__ == "__main__":
    main()
