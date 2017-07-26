from indy import ledger

import json
import pytest
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.mark.asyncio
async def test_build_claim_def_request_works_for_correct_data_json(cleanup_storage):
    identifier = "identifier"
    signature_type = "CL"
    schema_seq_no = 1
    data = {
        "primary": {
            "n": "1",
            "s": "2",
            "rms": "3",
            "r": {
                "name": "1"
            },
            "rctxt": "1",
            "z": "1"
        }
    }

    expected_response = {
        "identifier": "identifier",
        "operation": {"ref": 1,
                      "data": '{"primary": {"n": "1", "s": "2", "rms": "3",'
                              ' "r": {"name": "1"}, "rctxt": "1", "z": "1"}}',
                      "type": "102",
                      "signature_type": "CL"}}

    response = json.loads(
        await ledger.build_claim_def_txn(
            identifier, schema_seq_no, signature_type, json.dumps(data)))
    assert expected_response.items() <= response.items()
