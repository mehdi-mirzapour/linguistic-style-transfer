from datetime import datetime as dt

logger_name = "linguistic_style_transfer"

experiment_timestamp = dt.now().strftime("%Y%m%d%H%M%S")
vocab_size = None

embedding_size = 300
max_sequence_length = 20
validation_interval = 1
tsne_sample_limit = 1000

save_directory = "./saved-models/{}".format(experiment_timestamp)
classifier_save_directory = "./saved-models-classifier/{}".format(experiment_timestamp)

all_style_embeddings_path = save_directory + "/all_style_embeddings.pkl"
all_content_embeddings_path = save_directory + "/all_content_embeddings.pkl"
all_shuffled_labels_path = save_directory + "/all_shuffled_labels_path.pkl"
label_mapped_style_embeddings_path = save_directory + "/label_mapped_style_embeddings.pkl"

style_embedding_plot_file = "tsne_embeddings_plot_style.svg"
content_embedding_plot_file = "tsne_embeddings_plot_content.svg"
style_embedding_custom_plot_file = "tsne_embeddings_custom_plot_style.svg"
content_embedding_custom_plot_file = "tsne_embeddings_custom_plot_content.svg"

unk_token = "<unk>"
sos_token = "<sos>"
eos_token = "<eos>"
predefined_word_index = {
    unk_token: 0,
    sos_token: 1,
    eos_token: 2,
}

bleu_score_weights = {
    1: (1.0, 0.0, 0.0, 0.0),
    2: (0.5, 0.5, 0.0, 0.0),
    3: (0.34, 0.33, 0.33, 0.0),
    4: (0.25, 0.25, 0.25, 0.25),
}

model_save_file = "linguistic_style_transfer_model.ckpt"
model_save_path = save_directory + "/" + model_save_file

vocab_size_save_file = "vocab_size_save_path.pkl"
vocab_save_file = "vocab.pkl"
text_tokenizer_file = "text_tokenizer.pkl"
vocab_size_save_path = save_directory + "/" + vocab_size_save_file
vocab_save_path = save_directory + "/" + vocab_save_file
text_tokenizer_path = save_directory + "/" + text_tokenizer_file
classifier_vocab_size_save_path = classifier_save_directory + "/" + vocab_size_save_file
classifier_vocab_save_path = classifier_save_directory + "/" + vocab_save_file
classifier_text_tokenizer_path = classifier_save_directory + "/" + text_tokenizer_file

index_to_label_dict_file = "index_to_label_dict.pkl"
label_to_index_dict_file = "label_to_index_dict.pkl"
index_to_label_dict_path = save_directory + "/" + index_to_label_dict_file
label_to_index_dict_path = save_directory + "/" + label_to_index_dict_file

average_label_embeddings_file = "average_label_embeddings.pkl"
average_label_embeddings_path = save_directory + "/" + average_label_embeddings_file

style_coordinates_file = "style_coordinates.pkl"
content_coordinates_file = "content_coordinates.pkl"
style_coordinates_path = save_directory + "/" + style_coordinates_file
content_coordinates_path = save_directory + "/" + content_coordinates_file

validation_scores_file = "validation_scores.txt"
validation_scores_path = save_directory + "/" + validation_scores_file
