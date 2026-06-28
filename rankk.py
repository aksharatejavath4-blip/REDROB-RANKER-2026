from datetime import datetime
def calculate_match_score(candidate):
    profile = candidate.get("profile", {})
    skills_list = candidate.get("skills", [])
    signals = candidate.get("redrob_signals", {})
    career_history = candidate.get("career_history", [])
    expert_zero_duration_count = 0
    for skill in skills_list:
        if skill.get("proficiency") == "expert" and skill.get("duration_months", 0) == 0:
            expert_zero_duration_count += 1           
    if expert_zero_duration_count >= 5: 
        return 0.0, "Disqualified: Impossible profile data (Skill Trap)."
    base_score = 0.0
    current_title = profile.get("current_title", "").lower()
    if any(title in current_title for title in {"ai engineer", "ml engineer", "machine learning engineer"}):
        base_score += 0.5
    elif "data scientist" in current_title:
        base_score += 0.3
    matched_skills = 0
    target_keywords = {"embeddings", "retrieval", "ranking", "vector database", "python", "nlp"}
    for skill in skills_list:
        if any(target in skill.get("name", "").lower() for target in target_keywords):
            matched_skills += 1
    base_score += min(matched_skills * 0.08, 0.5)
    response_rate = signals.get("recruiter_response_rate", 0.0)
    last_active_str = signals.get("last_active_date", "2026-01-01")
    try:
        last_active_dt = datetime.strptime(last_active_str, "%Y-%m-%d")
        days_inactive = (datetime(2026, 6, 28) - last_active_dt).days
        activity_multiplier = 1.0 if days_inactive < 30 else 0.5
    except Exception:
        activity_multiplier = 0.5
    final_score = base_score * response_rate * activity_multiplier
    reasoning = (f"{profile.get('current_title', 'Engineer')} with {profile.get('years_of_experience')} yrs exp; "
                 f"matched {matched_skills} core skills; response rate {round(response_rate, 2)}.")
    return final_score, reasoning
