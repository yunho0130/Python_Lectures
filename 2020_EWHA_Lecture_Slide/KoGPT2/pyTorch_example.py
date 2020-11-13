import torch
from kogpt2.pytorch_kogpt2 import get_pytorch_kogpt2_model
from gluonnlp.data import SentencepieceTokenizer
from kogpt2.utils import get_tokenizer

tok_path = get_tokenizer()
model, vocab = get_pytorch_kogpt2_model()
tok = SentencepieceTokenizer(tok_path)
sent = '2019년 한해를 보내며,'
toked = tok(sent)
while 1:
  input_ids = torch.tensor([vocab[vocab.bos_token],]  + vocab[toked]).unsqueeze(0)
  pred = model(input_ids)[0]
  gen = vocab.to_tokens(torch.argmax(pred, axis=-1).squeeze().tolist())[-1]
  if gen == '</s>':
      break
  sent += gen.replace('▁', ' ')
  toked = tok(sent)
sent
