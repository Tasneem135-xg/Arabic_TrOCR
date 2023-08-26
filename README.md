<a name="br1"></a> 

Opꢀcal character recogniꢀon For Arabic Text

This is a ﬁne tuning repo for TrOCR on Images that contains arabic text This ﬁle is

organized as following:

• TrOCR Architecture

• Dataset

• pipeline

a. Iniꢀal Dataset

b. Data Cleaning

c.

Preprocessing

d. Training Dataset

e. Training

f.

Evaluaꢀon

The Model Architecture

•

•

TrOCR paper: [hꢁps://arxiv.org/abs/2109.10282](https://arxiv.org/abs/2109.10282)

TrOCR documentaꢀon:

[hꢁps://huggingface.co/transformers/master/model_doc/trocr.html](https://huggingface.co/transformers/master/model_doc/trocr.html)

TrOCR Tutorial :

•

[hꢁps://github.com/NielsRogge/Transformers-Tutorials/tree/master/TrOCR](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/TrOCR)



<a name="br2"></a> 

Pipeline

Iniꢀal Dataset

•

•

•

data contains Faulty Images with croped characters that needs to be removed

All Images contains one line and have the same background (distribuꢀon)

sentence length is falls between 9-13 tokens

Data Cleaning

The dataset had croped text that needed to be removed from the training data this was done using

1\. Detect the Height of the characters

2\. Compare Maximum character Height to choose threshold = 17 3. Remove the

Faulty Images 8%leaving 92%for training

example:

Data Preprocessing

Removing Background and enhance the characters

1\. convert image to greyscale

2\. Binarize image threshold = 110

Output:

Training Dataset

Due to Limited Time and Computaꢀonal Power espicially RAM A random Sample was taken from the

iniꢀal data with :

•

•

training 1400 sample

evaluaꢀon 600 sample



<a name="br3"></a> 

Training

The training used HuggingFace's Seq2SeqTrainer :

[hꢁps://huggingface.co/docs/transformers/main_classes/trainer#transformers.Seq2SeqTrainer](https://huggingface.co/docs/transformers/main_classes/trainer#transformers.Seq2SeqTrainer)

choosing the encoder and decoder for the Task

\# choosing feature extractor and tokenizer

feature\_extractor =

AutoFeatureExtractor.from\_pretrained("google/vitbase-patch16-384")

decoder\_tokenizer = AutoTokenizer.from\_pretrained('xlm-roberta-base')

processor =TrOCRProcessor(feature\_extractor=feature\_extractor,

tokenizer=decoder\_tokenizer)

Train parameters

Note : some of these values were chosen to reduce Memory and computaꢀonal power due to hardware

limitaꢀon

• maxlength for seq = 20

• batch size =3

• epoch =3

Evaluaꢀon

Character Error Rate (CER) metric for evaluaꢀng the performance of a sequence-to-sequence model

[hꢁps://huggingface.co/spaces/evaluate-metric/cer](https://huggingface.co/spaces/evaluate-metric/cer)

