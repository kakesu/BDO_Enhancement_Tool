#- * -coding: utf - 8 - * -
"""
🛳 NSWCP 🚢 Code 324 🛳

@author: ☙ Ryan McConnell ♈♑ ryan.mcconnell@navy.mil ❧
"""
from common import ItemStore, EnhanceSettings
from utilities import Settings, chain_iter

MEMORY_FRAG_COST = 1740000
P_CRON_STONE_COST = 2000000
P_CLEANSE_COST = 100000


def convert_0002(state_obj):
    P_NUM_FS = 'num_fs'
    P_CRON_STONE_COST = 'cost_cron'
    P_CLEANSE_COST = 'cost_cleanse'
    P_FAIL_STACKERS = 'fail_stackers'
    P_COST_CONC_W = 'cost_conc_w'
    P_COST_BS_W = 'cost_bs_w'
    P_R_ENHANCE_ME = 'r_enhance_me'
    P_FS_EXCEPTIONS = 'fs_exceptions'
    P_COST_CONC_A = 'cost_conc_a'
    P_R_FAIL_STACKERS = 'r_fail_stackers'
    P_COST_BS_A = 'cost_bs_a'
    P_ENHANCE_ME= 'enhance_me'
    P_FS_COUNTS = 'fail_stackers_count'
    P_COST_MEME = 'cost_meme'

    item_shop = {'items':{
        ItemStore.P_MEMORY_FRAG: state_obj.pop(P_COST_MEME),
        ItemStore.P_CONC_WEAPON: state_obj.pop(P_COST_CONC_W),
        ItemStore.P_CONC_ARMOR: state_obj.pop(P_COST_CONC_A),
        ItemStore.P_BLACK_STONE_WEAPON: state_obj.pop(P_COST_BS_W),
        ItemStore.P_BLACK_STONE_ARMOR: state_obj.pop(P_COST_BS_A)
    }
    }

    state_obj[EnhanceSettings.P_ITEM_STORE] = item_shop

    return state_obj

def convert_0010(state_obj):
    P_NUM_FS = 'num_fs'
    P_CRON_STONE_COST = 'cost_cron'
    P_CLEANSE_COST = 'cost_cleanse'
    P_FAIL_STACKERS = 'fail_stackers'
    P_COST_CONC_W = 'cost_conc_w'
    P_COST_BS_W = 'cost_bs_w'
    P_R_ENHANCE_ME = 'r_enhance_me'
    P_FS_EXCEPTIONS = 'fs_exceptions'
    P_COST_CONC_A = 'cost_conc_a'
    P_R_FAIL_STACKERS = 'r_fail_stackers'
    P_COST_BS_A = 'cost_bs_a'
    P_ENHANCE_ME= 'enhance_me'
    P_FS_COUNTS = 'fail_stackers_count'
    P_COST_MEME = 'cost_meme'


    P_fail_stackers = state_obj[P_FAIL_STACKERS]
    P_r_fail_stackers = state_obj[P_R_FAIL_STACKERS]
    P_enhanceme = state_obj[P_ENHANCE_ME]
    P_r_enhanceme = state_obj[P_R_ENHANCE_ME]


    for gear_obj in chain_iter(P_fail_stackers, P_r_fail_stackers, P_enhanceme, P_r_enhanceme):
        cost = gear_obj.pop('cost')
        gear_obj['base_item_cost'] = cost

    return state_obj

converters = {
    '0.0.0.2': lambda x: convert_0010(convert_0002(x)),
    '0.0.1.0': convert_0010
}
