import os
import wandb
from datetime import datetime

def init_wandb(run_name_prefix: str, config: dict = None, tags: list = None):
    """
    Initialize Weights & Biases run with standardized naming and configs.
    """
    # Load settings from environment or set defaults
    project_name = os.getenv("WANDB_PROJECT", "banlegit-cite")
    entity = os.getenv("WANDB_ENTITY", None) # Default user workspace
    
    # Generate run name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_name = f"{run_name_prefix}_{timestamp}"
    
    run = wandb.init(
        project=project_name,
        entity=entity,
        name=run_name,
        config=config,
        tags=tags or [],
        reinit=True
    )
    print(f"Initialized W&B run: {run_name} (ID: {run.id})")
    return run

def log_experiment_artifact(run, artifact_name: str, artifact_type: str, file_path: str, description: str = None):
    """
    Log a file or directory as a W&B Artifact for reproducibility/provenance.
    """
    artifact = wandb.Artifact(
        name=artifact_name,
        type=artifact_type,
        description=description
    )
    
    if os.path.isdir(file_path):
        artifact.add_dir(file_path)
    else:
        artifact.add_file(file_path)
        
    run.log_artifact(artifact)
    print(f"Logged artifact {artifact_name} from {file_path}")
