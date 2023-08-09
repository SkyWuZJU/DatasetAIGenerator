
role_desc_in_depth = """I want you act as a Prompt Rewriter. And both Chinese and English are your mother language.

Your objective is to rewrite a given prompt into a more complex version to make those famous AI systems (e.g., ChatGPT and GPT4) a bit harder to handle.
But the rewritten prompt must be reasonable and must be understood and responded by humans, especially Chinese people.
Besides, the #Rewritten Prompt# must be in Chinese.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt#:. 
Also, please do not omit the input in #Given Prompt#.
"""


add_constraints = role_desc_in_depth + """
You SHOULD complicate the given prompt using the following method:
Please add one more constraints/requirements into #Given Prompt#
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
‘#Given Prompt#’, ‘#Rewritten Prompt#’, ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in #Rewritten Prompt#

#Given Prompt#:
{initial_prompt}
#Rewritten Prompt#:"""

deepening = role_desc_in_depth + """You SHOULD complicate the given prompt using the following method:

If #Given Prompt# contains inquiries about certain issues, the depth and breadth of the inquiry can be increased.
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
‘#Given Prompt#’, ‘#Rewritten Prompt#’, ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in #Rewritten Prompt#

#Given Prompt#:
{initial_prompt}
#Rewritten Prompt#:"""

concretizing = role_desc_in_depth + """You SHOULD complicate the given prompt using the following method:

Please replace general concepts with more specific concepts.
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
‘#Given Prompt#’, ‘#Rewritten Prompt#’, ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in #Rewritten Prompt#

#Given Prompt#:
{initial_prompt}
#Rewritten Prompt#:"""

increase_reasoning = role_desc_in_depth + """
You SHOULD complicate the given prompt using the following method:

If #Given Prompt# can be solved with just a few simple thinking processes, you can rewrite it to explicitly request multiple-step reasoning.
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
‘#Given Prompt#’, ‘#Rewritten Prompt#’, ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in #Rewritten Prompt#

#Given Prompt#:
{initial_prompt}
#Rewritten Prompt#:"""

complicate_input = """"""

enhance_diversity = """I want you act as a Prompt Creator. And both Chinese and English are your mother language.

Your goal is to draw inspiration from the #Given Prompt# to create a brand new prompt in Chinese.

This new prompt should belong to the same domain as the #Given Prompt# but be even more rare.
The LENGTH and difficulty level of the #Created Prompt# should be similar to that of the #Given Prompt#. 
The #Created Prompt# must be reasonable and must be understood and responded by humans.
‘#Given Prompt#’, ‘#Created Prompt#’, ‘given prompt’ and ‘created prompt’ are not allowed to appear in #Created Prompt#.

#Given Prompt#:
{initial_prompt}
#Created Prompt#:"""


equal_judger = """Here are two Instructions to ChatGPT AI, do you think they are equal to each other, which meet the following requirements:
1. They have same constraints and requirments.
2. They have same depth and breadth of the inquiry.
The First Prompt: {FirstPrompt}
The Second Prompt: {SecondPrompt}
Your Judgement (Just answer: Equal or Not Equal. No need to explain the reason.):"""