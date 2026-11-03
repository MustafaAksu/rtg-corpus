# DYAD OPEN20 bounds preflight: R1-R3 verification on PI Windows/PowerShell.
# SESSION preparation only; no Stage-3 certification or scientific adoption.
$ErrorActionPreference = "Stop"
$root = (git rev-parse --show-toplevel).Trim()
Push-Location $root
try {
    $script = "evidence/dyad/scripts/dyad_open20_an_bounds_prep.py"
    $out = "evidence/dyad/open20-an/bounds_preflight_session.json"
    $expected = "708049c9da39b2ad866639feed089fe2aeea326aab032d1744c3cc7545b039eb"
    $actual = (Get-FileHash $script -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $expected) { throw "Unexpected preflight script SHA-256: $actual" }

    python -I -B $script --self-test
    if ($LASTEXITCODE -ne 0) { throw "Self-test failed with exit $LASTEXITCODE" }

    python -I -B $script --out $out
    if ($LASTEXITCODE -ne 0) { throw "Positive preflight failed with exit $LASTEXITCODE" }

    $j = Get-Content $out -Raw | ConvertFrom-Json
    if ($j.Stage3 -ne "NOT_CERTIFIED" -or !$j.exact_quadratic_return_zero_checked) {
        throw "Missing preflight scope or exact F2 gate"
    }
    if ($j.forward_template.E5_uniform_tail_U1_upper -ne "1.25079517787224E+63" -or
        $j.forward_template.E5_uniform_tail_U2_upper -ne "1.25080479490175E+63") {
        throw "R1 corrected E5 outputs differ from reviewed outward values"
    }
    if ($j.script_sha256 -ne $expected) { throw "Output script hash mismatch" }

    foreach ($c in @("wrong-alpha", "wrong-root", "wrong-tail", "degree2")) {
        python -I -B $script --control $c
        if ($LASTEXITCODE -ne 1) {
            throw "Negative control $c exited $LASTEXITCODE (expected exactly 1)"
        }
    }
    Write-Output "RESULT PASS: positive, self-test, exact F2, corrected E5, four real negative controls"
    Write-Output "Evidence: $out"
}
finally {
    Pop-Location
}
