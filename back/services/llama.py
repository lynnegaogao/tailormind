import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class Llama:
    def __init__(self, model_path: str, device: str):
        self.model_path = model_path
        self.device = device
        self.dtype = torch.float16
        # 模型和分词器加载
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_path,
            trust_remote_code=True,
            low_cpu_mem_usage=True,
            torch_dtype=self.dtype,
        ).to(self.device).eval()
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_path,
            trust_remote_code=True,
            use_fast=True
        )
        # 设置pad_token为eos_token
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate(self, query: str, max_length: int = 4096):
        # 对 query 进行编码
        inputs = self.tokenizer(query, return_tensors="pt", padding=True).to(self.device)
        
        # 生成文本
        output_ids = self.model.generate(
            inputs.input_ids,
            max_length=max_length,
            pad_token_id=self.tokenizer.eos_token_id,
            num_beams=5,
            no_repeat_ngram_size=2,
            early_stopping=True,
        )
        
        # 解码生成的文本
        generated_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True,clean_up_tokenization_spaces=False)
        
        # 剔除输入文本部分，仅返回模型的回答
        answer_start_idx = len(query)
        answer = generated_text[answer_start_idx:].strip()
        
        return {"text": answer}

    
    
# llama=Llama(model_path='E:\\Vis24-TailorMind\\tailormind\\back\\sft_v2.0',device='cuda:0')
# response=llama.generate(query="Give a multiple choice question on Attention Mechanism.")
# print(response)
# response2=llama.generate(query="Please give the correct option.")
# print(response2)
# response3=llama.generate(query="Please explain each option.")
# print(response3)