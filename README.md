# REDROB-RANKER-2026
TECH VIBER'S Submission for the Redrob Intelligent candidate discovery &amp; ranking challenge.

team_name: "Tech Viber" 

primary_contact:

  name: AKSHARA TEJAVATH
  email: aksharatetavath4@gmail.com
  
team_members:

  - name: Akshara Tejavath
    email: aksharatetavath4@gmail.com
    role: Team Lead & Lead ML Engineer
  - name: Gaddam Akshitha
    email: gaddamakshitha02@gamil.com
    role: Data & Performance Engineer
  - name: Guguloth Niharika
    email: sanjayguguloth2009@gmail.com
    role: QA & Anti-Fraud Specialist
  - name: Kalva Saisri
    email: kalvasaisri79@gmail.com
    role: Product, DevOps & Explainability Engineer
    
github_repo: https://github.com/aksharatejavath4-blip/REDROB-RANKER-2026/new/main 

reproduce_command: "python rank.py --candidates ./candidates.jsonl.gz --out ./sample_submission.csv"

compute:
  platform: "Windows Laptop"                    
  cpu_cores: 8                                  
  ram_gb: 16                                    
  python_version: "3.11.4"                      
  os: "Windows 11"                              
  uses_gpu_for_inference: false                 
  has_network_during_ranking: false             
  pre_computation_required: false               
  pre_computation_time_minutes: 0 
  
ai_tools_used:
  - "Gemini"  
ai_usage_summary: |
  Used Gemini to design the pipeline stream layout, formulate basic keyword heuristics, 
  and ensure strict compliance with computing budget requirements.
methodology_summary: |
  A lightweight, multi-stage pipeline built purely in Python to stream the candidate dataset row-by-row. 
  It implements strict data-integrity logic blocks to instantly detect and eliminate honeypot profile traps. 
  Validated candidates are evaluated using deterministic scoring metrics (50% title match, 50% technical skill overlap) modified continuously by interactive platform behavioral signals.

declarations:
  read_submission_spec: true        
  code_is_original_work: true       
  no_collusion: true                
  honeypot_check_done: true         
  reproduction_tested: true


##OUTPUT##

 <img width="1083" height="1041" alt="Image" src="https://github.com/user-attachments/assets/60801dd1-719f-4a00-9e02-39b4458ef6de" />
