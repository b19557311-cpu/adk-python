# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A beginner-friendly, multi-agent Researcher & Formatter workflow using ADK 2.0."""

import os

from google.adk import Agent
from google.adk import Workflow
from google.adk.tools.google_search_tool import google_search

# --- LEARNING NOTE: Multi-Provider Support ---
# This workflow is configured to natively run on Gemini models using the
# google-genai integration. If you want to use other model providers in your
# agents, you can change the `model` argument on individual Agents.
#
# Example (Google Gemini - Default):
#   model="gemini-2.5-flash"
#
# Example (OpenAI - Requires setting OPENAI_API_KEY):
#   model="openai/gpt-4o"
#
# Example (Anthropic - Requires setting ANTHROPIC_API_KEY):
#   model="anthropic/claude-3-5-sonnet"

# 1. THE RESEARCHER AGENT
# This agent takes a topic, does deep research, and is equipped with Google Search
# so it can look up real-time information if an internet-connected key is available.
researcher_agent = Agent(
    name="researcher_agent",
    model=os.environ.get("ADK_RESEARCH_MODEL", "gemini-2.5-flash"),
    instruction="""
    You are a professional and extremely thorough Research Assistant.
    Your goal is to gather detailed, accurate, and comprehensive information about the requested topic.

    If needed and available, use the google_search tool to verify facts, find real-world statistics, or get recent news.
    Ensure you output a detailed compilation of facts, descriptions, and reliable context.
    Do not worry about making the output pretty; focus purely on depth and factual richness.
    """,
    tools=[google_search],
)

# 2. THE FORMATTER AGENT
# This agent takes raw research data and formats it into a highly polished, structured report.
formatter_agent = Agent(
    name="formatter_agent",
    model=os.environ.get("ADK_FORMAT_MODEL", "gemini-2.5-flash"),
    instruction="""
    You are a skilled Content Designer and Technical Writer.
    Your job is to take the detailed raw research information provided to you and transform it into a highly polished, professional document.

    Format the research with:
    - An engaging title and executive summary.
    - Well-structured sections with headings (using Markdown).
    - Bullet points, bold text, or tables to highlight key points.
    - A brief conclusion.

    Make the layout extremely clear, modern, and easy to read for any audience.
    """,
)

# 3. THE WORKFLOW
# In ADK 2.0, Workflows chain nodes together in a directed graph.
# Here, we specify a simple linear sequence:
# START -> researcher_agent -> formatter_agent -> END.
# Under the hood, ADK manages the "handoff" automatically, passing the Researcher's
# output directly as the input to the Formatter.
root_agent = Workflow(
    name="researcher_workflow",
    edges=[
        ("START", researcher_agent),
        (researcher_agent, formatter_agent),
    ],
)
