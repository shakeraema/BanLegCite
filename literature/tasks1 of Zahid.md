Task Checklist — Researcher B Phase 1 Shadow Work
 CI/DevOps Setup
 Create GitHub Actions workflow .github/workflows/ci.yml
 Data Version Control (DVC) Setup
 Create DVC helper script scripts/utils/dvc_setup.py
 Initialize DVC on repository
 Weights & Biases (W&B) Setup
 Create W&B helper script scripts/utils/wb_config.py
 Annotation Infrastructure (Label Studio) Setup
 Create setup shell script annotation/setup_label_studio.sh
 Create XML configuration template annotation/config.xml
 Scraper Framework Skeleton
 Create base scraper scripts/scraper/base_scraper.py
 Create DLR scraper scripts/scraper/dlr_scraper.py
 Create BLC scraper scripts/scraper/blc_scraper.py
 Create ALR scraper scripts/scraper/alr_scraper.py
 Create scraper orchestrator entrypoint scripts/scraper/main.py