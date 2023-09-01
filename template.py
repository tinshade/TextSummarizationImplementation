import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')





class InitialSetup:
    def __init__(self):
        self.setup_text='''
import setuptools
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "TextSummarizationImplementation"
AUTHOR_USER_NAME = "tinshade"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "tinshade98@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version =__version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for NLP app", 
    Long_description =long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src')
)
        '''
        self.project_name = 'text_summarizer'
        self.initial_file = '__init__.py'
        self.base_path = os.path.join(os.getcwd(), 'src', self.project_name)
        self.file_list = [
            os.path.join(self.base_path, self.initial_file),
            os.path.join(self.base_path, 'components',self.initial_file),
            os.path.join(self.base_path, 'utils', self.initial_file),
            os.path.join(self.base_path, 'utils', 'common.py'),
            os.path.join(self.base_path, 'logging', self.initial_file),
            os.path.join(self.base_path, 'config', self.initial_file),
            os.path.join(self.base_path, 'config','configuration.py'),
            os.path.join(self.base_path, 'pipeline',self.initial_file),
            os.path.join(self.base_path, 'entity',self.initial_file),
            os.path.join(self.base_path, 'constants',self.initial_file),
            os.path.join("research","trials.ipynb"),
            os.path.join("config","config.yaml"),
            "params.yaml",
            "app.py",
            "main.py",
            "Dockerfile",
            "requirements.txt",
            "setup.py",
        ]
        self.requriements = ['transformers', 'transformers[sentencepiece]', 'datasets==2.12.0', 'sacrebleu', 'rouge_score', 'py7zr', 'pandas', 'nltk', 'tqdm', 'PyYAML', 'matplotlib','torch', 'torchvision', 'torchaudio --index-url https://download.pytorch.org/whl/cu111', 'notebook','boto3','mypy-boto3-s3','python-box==6.0.2','ensure==1.0.2','fastapi==0.78.0','uvicorn==0.18.3','Jinja2==3.1.2', '-e .']
    
    def create_files(self, filepath, filename):
        with open(filepath, 'w') as f:
            if filename == 'requirements.txt':
                for each in self.requriements:
                    f.write(f"{each}\n")
            elif filename == 'setup.py':
                f.write(self.setup_text)
            #Only create the file and nothing else
            logging.info(f"Creating empty file: {filepath}")
    
    def setup_structure(self, overwrite=False):
        print(self.file_list)
        for file in self.file_list:
            filepath = Path(file)
            directory, filename = os.path.split(filepath)
            
        
            if directory:
                os.makedirs(directory,exist_ok=True)
                logging.info(f"Creating directory: {directory} for file: {filename}")
            if overwrite:
                self.create_files(filepath, filename)
            else:
                if (not os.path.exists(filepath)) or (os.path.getsize(filepath)  == 0):
                    self.create_files(filepath, filename)
            
                else:
                    logging.info(f"Already exits: {filename}")








if __name__ == "__main__":
    setup = InitialSetup()
    setup.setup_structure(overwrite=True)