from git import Repo
import logging
import os
import consts
import shutil

def reset_repo():
    if os.path.exists(consts.REPO_PATH):
        logging.info('Removing directory ' + consts.REPO_PATH)
        shutil.rmtree(consts.REPO_PATH)

    logging.info('Initializing repo at ' + consts.REPO_PATH)
    return Repo.init(consts.REPO_PATH)

def check_repo():
    if os.path.exists(consts.REPO_PATH):
        logging.info('Repo Directory found')
        try:
            repo = Repo(consts.REPO_PATH)
            logging.info('Repo found')
            return repo
        except Exception as e:
            logging.info('Repo does not exist')
    return reset_repo()

def stage_all():
    repo = Repo(consts.REPO_PATH)
    repo.git.reset('HEAD', '.')
    logging.info('Staging all files')
    repo.git.add(consts.BASE_MD)
    repo.git.add(consts.DATA_PATH)
    repo.git.add(consts.PLAYLIST_PATH)
    return repo.index.diff('HEAD')

def commit():
    repo = Repo(consts.REPO_PATH)
    logging.info('Committing')
    repo.index.commit('Update')

def push():
    repo = Repo(consts.REPO_PATH)
    logging.info('Pushing')
    origin = repo.remote('origin')
    origin.push()
