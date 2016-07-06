import os

# # LeiCA modules
from learning.learning_predict_data_wf import learning_predict_data_2samp_wf
from learning.learning_variables import in_data_name_list, subjects_selection_crit_dict, \
    target_list



use_n_procs = 6
plugin_name = 'MultiProc'


working_dir = '/data/liem-3/LeiCA_LIFE_learning_wd/wd_learning_ncd_norm'
ds_dir = '/scr/adenauer2/Franz/LeiCA_LIFE/learning_out_ncd_norm/training_life_only'
aggregated_subjects_dir = '/scr/adenauer2/Franz/LeiCA_LIFE/learning_out/vectorized_aggregated_data'

aggregated_subjects_dir_nki = '/scr/adenauer2/Franz/LeiCA_NKI/learning_out/vectorized_aggregated_data'
subjects_selection_crit_dict_nki = {}
subjects_selection_crit_dict_nki = None #['adult'] = ["age >= 18", "n_TRs > 890"]
subjects_selection_crit_name_nki = None #'adult'


subjects_selection_crit_names_list = ['bothSexes_neuH_FD06_ncd_norm']


# LIFE only training
run_2sample_training = False
learning_predict_data_2samp_wf(working_dir=working_dir,
                               ds_dir=ds_dir,
                               in_data_name_list=in_data_name_list,
                               subjects_selection_crit_dict=subjects_selection_crit_dict,
                               subjects_selection_crit_names_list=subjects_selection_crit_names_list,
                               aggregated_subjects_dir=aggregated_subjects_dir,
                               target_list=target_list,
                               use_n_procs=use_n_procs,
                               plugin_name=plugin_name,
                               confound_regression=[False],
                               run_cv=True,
                               n_jobs_cv=5,
                               run_tuning=False,
                               run_2sample_training=run_2sample_training,
                               aggregated_subjects_dir_nki=aggregated_subjects_dir_nki,
                               subjects_selection_crit_dict_nki=subjects_selection_crit_dict_nki,
                               subjects_selection_crit_name_nki=subjects_selection_crit_name_nki)


