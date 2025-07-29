from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ChatModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
        self.chat_history = {}

    def get_response(self, user_input, session_id="default"):
        # Encode input
        new_input_ids = self.tokenizer.encode(
            user_input + self.tokenizer.eos_token, return_tensors='pt'
        )

        # Retrieve or initialize history
        history_ids = self.chat_history.get(session_id)
        bot_input_ids = torch.cat([history_ids, new_input_ids], dim=-1) if history_ids is not None else new_input_ids

        # Generate a response
        output_ids = self.model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=self.tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95
        )

        # Save updated chat history
        self.chat_history[session_id] = output_ids

        # Extract only new response
        response_ids = output_ids[:, bot_input_ids.shape[-1]:]
        reply = self.tokenizer.decode(response_ids[0], skip_special_tokens=True)

        return reply.strip()
