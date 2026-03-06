"""
Gemini AI Provider
------------------

This module implements a Gemini-based LLM provider that conforms to the
LLMProvider interface used across the agent framework. The provider acts as a
wrapper around Google's Gemini API and exposes a unified `generate()` method
so that the rest of the system can interact with Gemini models in the same
way it interacts with other LLM providers such as OpenAI or OpenRouter.

Purpose
-------
The goal of this provider abstraction is to decouple the core agent logic
from any specific language model API. By implementing the common
LLMProvider interface, the Gemini provider can be plugged into the system
without requiring changes to higher-level agent components.

Key Responsibilities
--------------------
• Initialize and configure the Gemini client using an API key.
• Convert internal ChatMessage objects into the format expected by Gemini.
• Send chat completion requests to Gemini models.
• Extract and return the generated response text.
• Handle API errors and retry logic when necessary.
• Maintain compatibility with the framework's standardized LLM interface.

Architecture Role
-----------------
The provider is part of a modular LLM backend system:

        LLMProvider (base interface)
                │
        ┌───────┼─────────┐
        │       │         │
     OpenAI   Gemini   Other Providers

Each provider implements the same `generate(messages)` method so the agent
pipeline can switch models without modifying its core logic.

Advantages of this design include:
• Provider interchangeability
• Centralized error handling
• Clean separation between model APIs and agent logic
• Easier experimentation with different LLMs

Usage
-----
The provider is instantiated with a Gemini model name and API credentials.
Once initialized, the `generate()` method can be used to obtain responses
from the model based on a list of conversation messages.

Example:

    provider = GeminiChatProvider(
        model="gemini-1.5-pro",
        api_key="YOUR_API_KEY"
    )

    response = provider.generate(messages)

The returned value is the generated text response from the Gemini model.

Notes
-----
This module focuses only on communication with Gemini models. Higher-level
agent behavior, prompt orchestration, and reasoning pipelines are handled
by other components in the framework.
"""