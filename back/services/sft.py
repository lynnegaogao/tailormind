import torch
from transformers import AutoModelForCausalLM, AutoTokenizer,GenerationConfig


class MinderLLM:
    def __init__(self, model_path: str, device: str):
        self.model_path = "E:\\Vis24-TailorMind\\tailormind\\back\\sft_v3.0" 
        # self.model_path = "E:\\Vis24-TailorMind\\tailormind\\back\\sft_v1.0" 
        self.device = device
        self.dtype = torch.float16
        # 模型加载
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_path,
            trust_remote_code=True,
            low_cpu_mem_usage=True,
            torch_dtype=self.dtype,
        ).to(self.device).eval()
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True,
            use_fast=True)
        self.model.generation_config = GenerationConfig.from_pretrained(model_path)
        self.model.generation_config.user_token_id = 195
        self.model.generation_config.assistant_token_id = 196

    def generate(self, query: str):
        # 对 query 进行编码
        # input_prompt = '<s>' + query + '</s>'
        input_prompt = []
        input_prompt.append({"role":"user","content":query})
        response = self.model.chat(self.tokenizer,input_prompt)
        return {"text":response}
    