#!/usr/bin/env python3
import os
import sys
import json
import ollama

WORKSPACE = "/home/kessiathecreator/recovery_robot"
SYSTEM_PROMPT_PATH = os.path.join(WORKSPACE, "jarvis_system_prompt.txt")
OUTPUT_WAV = os.path.join(WORKSPACE, "response.wav")

def load_system_prompt():
    if os.path.exists(SYSTEM_PROMPT_PATH):
        with open(SYSTEM_PROMPT_PATH, "r") as f:
            return f.read().strip()
    return "You are Jarvis, a witty AI assistant. Keep responses ultra-short for automated systems."

def main():
    if len(sys.argv) < 2:
        user_query = input("\nAwaiting instructions, operator: ")
    else:
        user_query = " ".join(sys.argv[1:])

    system_instruction = load_system_prompt()
    print(f"\n[GGUF-Core] Querying lightweight text interface...")

    try:
        # Optimized for a 4GB RAM environment
        response = ollama.generate(
            model="qwen2.5:1.5b", 
            prompt=user_query,
            system=system_instruction
        )
        
        jarvis_text = response['response']
        print(f"\nJarvis: {jarvis_text}")
        
        # Ensure the voice_engine folder exists before writing
        os.makedirs(os.path.join(WORKSPACE, "voice_engine"), exist_ok=True)
        
        # Output text file for your lightweight ONNX engine to synthesize
        with open(os.path.join(WORKSPACE, "voice_engine/input.txt"), "w") as f:
            f.write(jarvis_text)
            
        print("[System] Text cached for ONNX voice generation pipeline.")

    except Exception as e:
        print(f"\nSystem Error processing core instruction: {e}")

if __name__ == "__main__":
    main()
