"""
ChatDev Assistant Integration for Source AI Mistral Edition

This module integrates ChatDev functionality into Source AI, providing:
- AI-powered code generation
- Debugging assistance
- Development workflow automation
- Code review and optimization

USAGE:
  from chatdev_assistant import ChatDevAssistant
  assistant = ChatDevAssistant(app)
  response = assistant.code_generation(prompt)
"""

import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Optional, Dict, Any, List


class ChatDevAssistant:
    """
    ChatDev Assistant for Source AI
    
    Provides AI-powered development assistance including:
    - Code generation and completion
    - Debugging and error analysis
    - Code review and optimization
    - Documentation generation
    - Test case generation
    """
    
    def __init__(self, app=None):
        self.app = app
        self.chatdev_path = None
        self._setup_chatdev()
    
    def _setup_chatdev(self):
        """Setup ChatDev path."""
        # Check if ChatDev is installed locally
        possible_paths = [
            Path(__file__).parent / "ChatDev",
            Path(__file__).parent.parent / "ChatDev",
            Path.home() / "ChatDev",
            Path("C:/ChatDev"),
        ]
        
        for path in possible_paths:
            if (path / "chatdev.py").exists():
                self.chatdev_path = path
                break
    
    def _run_chatdev(self, prompt: str, role: str = "Software Engineer") -> str:
        """Run ChatDev with a prompt and return the response."""
        if not self.chatdev_path:
            return self._generate_response_without_chatdev(prompt, role)
        
        try:
            # Create a temporary prompt file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
                f.write(f"Role: {role}\n\nPrompt: {prompt}")
                temp_file = f.name
            
            # Run ChatDev
            result = subprocess.run(
                ["python", str(self.chatdev_path / "chatdev.py"), temp_file],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            # Clean up
            os.unlink(temp_file)
            
            if result.returncode == 0:
                return result.stdout
            else:
                return f"ChatDev error: {result.stderr}"
        except Exception as e:
            return f"Error running ChatDev: {e}"
    
    def _generate_response_without_chatdev(self, prompt: str, role: str = "Software Engineer") -> str:
        """Generate response using the main LLM if ChatDev is not available."""
        if self.app:
            system_prompt = f"""
You are a {role} assisting with Source AI development.
You are an expert in Python, PyTorch, transformers, and AI development.
Provide detailed, actionable responses to development questions.
"""
            return self.app.generate_response(prompt, system=system_prompt)
        else:
            return f"ChatDev not available. Please install ChatDev from https://github.com/OpenBMB/ChatDev"
    
    def code_generation(self, task: str, language: str = "Python") -> str:
        """Generate code for a specific task."""
        prompt = f"""
Generate {language} code for the following task:

Task: {task}

Requirements:
1. Follow Python best practices
2. Include error handling
3. Add comments where necessary
4. Make it compatible with Source AI architecture
5. Use type hints

Provide the complete, working code.
"""
        return self._run_chatdev(prompt, role="Software Engineer")
    
    def debug_code(self, code: str, error: str = None) -> str:
        """Debug code and suggest fixes."""
        prompt = f"""
Debug the following code from Source AI:

Code:
{code}

Error (if any): {error}

Your task:
1. Identify the issue
2. Explain the root cause
3. Provide the fixed code
4. Suggest improvements

Be thorough and specific.
"""
        return self._run_chatdev(prompt, role="Debugging Expert")
    
    def optimize_code(self, code: str, focus: str = "performance") -> str:
        """Optimize code for performance, memory, or readability."""
        prompt = f"""
Optimize the following code for {focus}:

Code:
{code}

Focus area: {focus}

Provide:
1. Analysis of current performance
2. Optimized code
3. Explanation of changes
4. Expected improvements
"""
        return self._run_chatdev(prompt, role="Performance Engineer")
    
    def generate_tests(self, code: str, test_type: str = "unit") -> str:
        """Generate test cases for code."""
        prompt = f"""
Generate {test_type} tests for the following code:

Code:
{code}

Test type: {test_type}

Requirements:
1. Use pytest framework
2. Test edge cases
3. Include assertions
4. Test both success and failure scenarios

Provide complete test code.
"""
        return self._run_chatdev(prompt, role="QA Engineer")
    
    def code_review(self, code: str) -> str:
        """Review code and suggest improvements."""
        prompt = f"""
Review the following code from Source AI:

Code:
{code}

Provide a comprehensive review including:
1. Code quality assessment
2. Potential bugs
3. Performance issues
4. Security concerns
5. Style improvements
6. Best practice violations

Be specific and provide examples.
"""
        return self._run_chatdev(prompt, role="Senior Developer")
    
    def explain_code(self, code: str) -> str:
        """Explain how code works."""
        prompt = f"""
Explain the following code from Source AI in detail:

Code:
{code}

Provide:
1. High-level overview
2. Line-by-line explanation
3. Purpose of each component
4. How it integrates with the rest of Source AI
"""
        return self._run_chatdev(prompt, role="Technical Writer")
    
    def generate_documentation(self, code: str) -> str:
        """Generate documentation for code."""
        prompt = f"""
Generate comprehensive documentation for the following code:

Code:
{code}

Documentation should include:
1. Module/function purpose
2. Parameters and return values
3. Usage examples
4. Dependencies
5. Error handling
6. Performance considerations

Format as Markdown.
"""
        return self._run_chatdev(prompt, role="Technical Writer")
    
    def suggest_features(self, context: str) -> str:
        """Suggest new features for Source AI."""
        prompt = f"""
Suggest new features for Source AI based on the following context:

Context: {context}

Provide:
1. 3-5 feature ideas
2. Implementation complexity for each
3. Expected benefits
4. Potential challenges
5. Priority ranking
"""
        return self._run_chatdev(prompt, role="Product Manager")


class ChatDevCLICommands:
    """ChatDev-specific CLI commands."""
    
    def __init__(self, app, assistant: ChatDevAssistant):
        self.app = app
        self.assistant = assistant
    
    def handle_command(self, command: str, args: List[str]) -> str:
        """Handle ChatDev-specific commands."""
        cmd = command.lower()
        
        if cmd in ['code', 'generate', 'write']:
            if len(args) >= 1:
                task = ' '.join(args)
                return self.assistant.code_generation(task)
            else:
                return "Usage: code <task> - Generate code for a task"
        
        elif cmd in ['debug', 'fix']:
            if len(args) >= 1:
                code = ' '.join(args)
                return self.assistant.debug_code(code)
            else:
                return "Usage: debug <code> - Debug code"
        
        elif cmd in ['optimize', 'improve']:
            if len(args) >= 1:
                code = ' '.join(args)
                focus = args[0] if len(args) > 1 else "performance"
                return self.assistant.optimize_code(code, focus)
            else:
                return "Usage: optimize <code> [focus] - Optimize code"
        
        elif cmd in ['test', 'tests']:
            if len(args) >= 1:
                code = ' '.join(args)
                return self.assistant.generate_tests(code)
            else:
                return "Usage: test <code> - Generate tests for code"
        
        elif cmd in ['review', 'audit']:
            if len(args) >= 1:
                code = ' '.join(args)
                return self.assistant.code_review(code)
            else:
                return "Usage: review <code> - Review code"
        
        elif cmd in ['explain', 'help']:
            if len(args) >= 1:
                code = ' '.join(args)
                return self.assistant.explain_code(code)
            else:
                return "Usage: explain <code> - Explain code"
        
        elif cmd in ['doc', 'docs']:
            if len(args) >= 1:
                code = ' '.join(args)
                return self.assistant.generate_documentation(code)
            else:
                return "Usage: doc <code> - Generate documentation"
        
        elif cmd in ['suggest', 'ideas']:
            if len(args) >= 1:
                context = ' '.join(args)
                return self.assistant.suggest_features(context)
            else:
                return "Usage: suggest <context> - Suggest new features"
        
        elif cmd in ['chatdev', 'dev']:
            return """
ChatDev Assistant Commands:
  code <task>          - Generate code
  debug <code>         - Debug code
  optimize <code>      - Optimize code
  test <code>          - Generate tests
  review <code>        - Review code
  explain <code>       - Explain code
  doc <code>           - Generate documentation
  suggest <context>    - Suggest new features
"""
        
        return None


class ChatDevGUIIntegration:
    """ChatDev integration for GUI."""
    
    def __init__(self, app, assistant: ChatDevAssistant):
        self.app = app
        self.assistant = assistant
    
    def add_chatdev_tab(self, notebook):
        """Add a ChatDev tab to the GUI notebook."""
        try:
            import tkinter as tk
            from tkinter import ttk, scrolledtext
            
            tab = ttk.Frame(notebook)
            notebook.add(tab, text="ChatDev Assistant")
            
            # Create layout
            self._create_chatdev_tab_layout(tab)
            
            return tab
        except ImportError:
            return None
    
    def _create_chatdev_tab_layout(self, tab):
        """Create the layout for the ChatDev tab."""
        # Task selection
        ttk.Label(tab, text="Select Task:").pack(pady=5)
        
        self.task_var = tk.StringVar(value="code")
        tasks = [
            ("Code Generation", "code"),
            ("Debug Code", "debug"),
            ("Optimize Code", "optimize"),
            ("Generate Tests", "test"),
            ("Code Review", "review"),
            ("Explain Code", "explain"),
            ("Documentation", "doc"),
            ("Suggest Features", "suggest"),
        ]
        
        for text, value in tasks:
            rb = ttk.Radiobutton(tab, text=text, variable=self.task_var, value=value)
            rb.pack(anchor=tk.W, pady=2)
        
        # Input
        ttk.Label(tab, text="Input:").pack(pady=(10, 5))
        self.input_text = scrolledtext.ScrolledText(tab, height=10, wrap=tk.WORD)
        self.input_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Output
        ttk.Label(tab, text="Output:").pack(pady=(0, 5))
        self.output_text = scrolledtext.ScrolledText(tab, height=15, wrap=tk.WORD, state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Button
        ttk.Button(tab, text="Run ChatDev", command=self._run_chatdev_task).pack(pady=5)
    
    def _run_chatdev_task(self):
        """Run the selected ChatDev task."""
        task = self.task_var.get()
        input_text = self.input_text.get(1.0, tk.END).strip()
        
        if not input_text:
            return
        
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Processing...\n")
        self.output_text.config(state=tk.DISABLED)
        
        # Run in background
        def run_task():
            try:
                if task == "code":
                    result = self.assistant.code_generation(input_text)
                elif task == "debug":
                    result = self.assistant.debug_code(input_text)
                elif task == "optimize":
                    result = self.assistant.optimize_code(input_text)
                elif task == "test":
                    result = self.assistant.generate_tests(input_text)
                elif task == "review":
                    result = self.assistant.code_review(input_text)
                elif task == "explain":
                    result = self.assistant.explain_code(input_text)
                elif task == "doc":
                    result = self.assistant.generate_documentation(input_text)
                elif task == "suggest":
                    result = self.assistant.suggest_features(input_text)
                else:
                    result = "Invalid task"
                
                self.output_text.config(state=tk.NORMAL)
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, result)
                self.output_text.config(state=tk.DISABLED)
            except Exception as e:
                self.output_text.config(state=tk.NORMAL)
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, f"Error: {e}")
                self.output_text.config(state=tk.DISABLED)
        
        import threading
        threading.Thread(target=run_task, daemon=True).start()


if __name__ == "__main__":
    print("ChatDev Assistant for Source AI")
    print("This module provides AI-powered development assistance.")
    print("Use with Source AI Mistral Edition.")
