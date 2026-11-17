import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import GEval
from deepeval.parameters import SdkParameters

factual_accuracy_metric = GEval(
    name="Factual Accuracy",
    criteria="Evaluate whether the output is completely factual and grounded.",
    evaluation_steps=[
        "Check all technical assertions against ground truth documents.",
        "Ensure no hallucinated parameters, code blocks, or system commands exist."
    ],
    evaluation_params=[SdkParameters.ACTUAL_OUTPUT, SdkParameters.RETRIEVAL_CONTEXT],
    threshold=0.8
)

def test_llm_output_quality():
    test_case = LLMTestCase(
        input="Explain connection pooling configuration.",
        actual_output="Use pgBouncer with transaction pooling mode for optimal throughput.",
        retrieval_context=["pgBouncer supports session, transaction, and statement pooling modes."]
    )
    assert_test(test_case, [factual_accuracy_metric])
