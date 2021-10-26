import configparser as ConfigParser
from dotenv import load_dotenv
import os

load_dotenv()

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read('config.ini')


def get_chain_names():
    return config['chains']['names']


def get_chain_targets():
    return config['chains']['targets']


def remove_chain_from_config(chain):
    chain_names_arr = config['chains']['names'].split()
    chain_index = chain_names_arr.index(chain)
    del chain_names_arr[chain_index]
    config['chains']['names'] = ' '.join(chain_names_arr)

    chains_targets_arr = config['chains']['targets'].split(", ")
    del chains_targets_arr[chain_index]
    config['chains']['targets'] = ', '.join(chains_targets_arr)



def get_pats():
    #Edited GitHub version - Include GitHub PATS below
    results = ["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", "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", "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", "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", "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"]
    return results
    #return os.getenv('GITHUB_PATS').split(" ")
