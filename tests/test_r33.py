from r33_cert.verifier import verify

def test_r33_certificate():
    r = verify()
    assert r["status"] == "PASS"
    assert r["k6_colorings_checked"] == 32768
