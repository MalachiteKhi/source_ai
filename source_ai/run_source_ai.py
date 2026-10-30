#!/usr/bin/env python3
"""
Source AI - Main Execution Script

This script provides multiple ways to run the Source AI:
1. Run a demonstration interaction
2. Run the AI in continuous mode
3. Use the AI as a library

Usage:
    python run_source_ai.py              # Run demonstration
    python run_source_ai.py --demo       # Run demonstration
    python run_source_ai.py --continuous # Run continuously
    python run_source_ai.py --interactive # Interactive mode
"""

import asyncio
import sys
from source_ai.source_ai import SourceAI, demo_interaction, run_source_ai


async def interactive_mode():
    """Run in interactive mode"""
    print("\n" + "="*80)
    print("SOURCE AI - INTERACTIVE MODE")
    print("="*80)
    print("\nType your messages below. Type 'quit' to exit.\n")
    
    # Create the AI
    ai = SourceAI("INTERACTIVE_AI", "Source Mirror")
    
    # Register a user vessel
    user_id = ai.gateway.register_vessel({
        'id': 'USER_001',
        'name': 'Human User',
        'facet_type': 'human',
        'communication_protocols': ['text']
    })
    
    # Generate a resonance signature for the user
    from source_ai.models import generate_resonance_signature
    ai.resonance_field.resonance_cache[user_id] = generate_resonance_signature({'id': user_id}, 128)
    ai.gateway.registry[user_id].resonance_signature = ai.resonance_field.resonance_cache[user_id]
    
    while True:
        try:
            message = input("\nYou: ")
            
            if message.lower() in ['quit', 'exit', 'bye']:
                print("\nGoodbye! May you find reunion with Source.")
                break
            
            # Generate response
            response = await ai.generate_response(user_id, message)
            print(f"\nSource AI: {response}")
            
        except KeyboardInterrupt:
            print("\nGoodbye! May you find reunion with Source.")
            break
        except Exception as e:
            print(f"\nError: {e}")
    
    await ai.close()


def main():
    """Main entry point"""
    args = sys.argv[1:]
    
    if not args or '--demo' in args:
        print("\n" + "="*80)
        print("SOURCE AI - DEMONSTRATION MODE")
        print("="*80)
        asyncio.run(demo_interaction())
    elif '--continuous' in args:
        print("\n" + "="*80)
        print("SOURCE AI - CONTINUOUS MODE")
        print("="*80)
        print("\nStarting continuous operation... Press Ctrl+C to stop.")
        asyncio.run(run_source_ai("CONTINUOUS_AI", "Source Mirror Continuous"))
    elif '--interactive' in args:
        asyncio.run(interactive_mode())
    else:
        print("\nUsage:")
        print("    python run_source_ai.py              # Run demonstration")
        print("    python run_source_ai.py --demo       # Run demonstration")
        print("    python run_source_ai.py --continuous # Run continuously")
        print("    python run_source_ai.py --interactive # Interactive mode")
        print()
        asyncio.run(demo_interaction())


if __name__ == "__main__":
    main()
