def abbreviation(a, b):
    n, m = len(a), len(b)
    idx = 0

    for j in range(n):
        print(a[j])
        if idx < m and (a[j] == b[idx] or a[j].upper() == b[idx]):
            idx += 1
        elif not a[j].islower():
            print(a[j])
            return "NO"
        print()
    if m == idx:
        return "YES"

    return "NO"


L = [[
    "RDWPJPAMKGRIWAPBZSYWALDBLDOFLWIQPMPLEMCJXKAENTLVYMSJNRJAQQPWAGVcGOHEWQYZDJRAXZOYDMNZJVUSJGKKKSYNCSFWKVNHOGVYULALKEBUNZHERDDOFCYWBUCJGbvqlddfazmmohcewjg",
    "RDPJPAMKGRIWAPBZSYWALDBLOFWIQPMPLEMCJXKAENTLVYMJNRJAQQPWAGVGOHEWQYZDJRAXZOYDMNZJVUSJGKKKSYNCSFWKVNHOGVYULALKEBUNZHERDOFCYWBUCJG"],
    ["MBQEVZPBjcbswirgrmkkfvfvcpiukuxlnxkkenqp", "MBQEVZP"],
    [
        "DINVMKSOfsVQByBnCWNKPRFRKMhFRSkNQRBVNTIKNBXRSXdADOSeNDcLWFCERZOLQjEZCEPKXPCYKCVKALNxBADQBFDQUpdqunpelxauyyrwtjpkwoxlrrqbjtxlkvkcajhpqhqeitafcsjxwtttzyhzvh",
        "DINVMKSOVQBBCWNKPRFRKMFRSNQRBVNTIKNBXRSXADOSNDLWFCERZOLQEZCEPKXPCYKCVKALNBADQBFDQU"],
    [
        "BFZZVHdQYHQEMNEFFRFJTQmNWHFVXRXlGTFNBqWQmyOWYWSTDSTMJRYHjBNTEWADLgHVgGIRGKFQSeCXNFNaIFAXOiQORUDROaNoJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMvSTGEQCYAJSFvbqivjuqvuzafvwwifnrlcxgbjmigkms",
        "BFZZVHQYHQEMNEFFRFJTQNWHFVXRXGTFNBWQOWYWSTDSTMJRYHBNTEWADLHVGIRGKFQSCXNFNIFAXOQORUDRONJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMSTGEQCYAJSF"],
    ["AQIUQVIPJDKYNEBPXFGVHCMFGvURORPRSTYQYJZCYJDNFRPRYTMZIsNDOJAOAGAEFRCDKUJBhdkedalbwoxxnoyowoxpdlelovibyiwat",
     "AQIUQVIPJDKYNEBPXFGVHCMFGURORPRSTYQYJZCYJDNFRPRYTMZINDOJAOAGAEFRCDKUJB"],
    [
        "HCPXJZTDXLWHYKHPPDFYFDJWTAETQLJCIIPVHMZHHOQTKONUHGYVKLXTFTBEMYAWXTCSwNJYALIGMIBDOWKIVStFATDOZCYSUCaATUWORPMTFPKTNHDSFWKRKBrXNBYICOZYDWLLElKKWTFAUSTZKFDCBQNYVcWKDHDMXJGFORwURHISYLBIZSOJXVRVBNPQLRJKIN",
        "HCPXJZTDXLWHYKHPPDFYFDJWTAETQLJCIIPVHMZHHOQTKONUHGYVKLXTFTBEMYAWXTCSNJYALIGMIBDOWKIVSFATDOZCYSUCATUWORPMTFPKTNHDSFWKRKBXNBYICOZYDWLLEKKWTFAUSTZKFDCBQNYVWKDHDMXJGFORURHISYLBIZSOJXVRVBNPQLRJKINIIOYB"],
    [
        "IZLAKtDFAITDNWMVQPDShQQFGTRIXDLNBQPZRpuRJMLLPHBMOWrNagJDPPREZSYBHIWKDHLkjPSEUWIVQYUfPPJYKCbPEKCSKBRIAAJTMDPAOLNWSQESOTRQZOFTMTTGTDTrWLPENHXHLDWAFNDZMIFlogtcddtulusydquboxquwmgcji",
        "IZLAKDFAITDNWMVQPDSQQFGTRIXDLNBQPZRRJMLLPHBMOWNJDPPREZSYBHIWKDHLPSEUWIVQYUPPJYKCPEKCSKBRIAAJTMDPAOLNWSQESOTRQZOFTMTTGTDTWLPENHXHLDWAFNDZMIF"],
    [
        "KRBPLVCTESRNPTCVNDMPTQYvFAWBGYPQHNXNAESRQMKFDZIEKVNZXSXKCFHQYCMMANPQFHWCEeNGOLWTUXZVMQNDZfRPLUFZcSTRLRYAZUKAZYXCVTNTNScSDFTBJSUKEQKZRDITZUCFVAPLCLTUWAXOnNHPYEOZDGWZPBJQBZEOFAeXTFJDWRHI",
        "KRBPVCTESRNPTCVNDMPTQYFWBGYPQHXNAESRQMFDZIEKVNZXSXKFHQYCMMANPQFHWCNGOLWTUXZVMQNDZRPLUFZSTRLRYAZUAZYXCVTNTNSSDTBJSUKEQKZRDITZUCFVAPCLTUWAXONHPYEOZDGWZPBJQBZEOAXTFJDWRHIPGQVCWODYNNV"],
    [
        "WOAECAAVWMSQMIMYMAPEVARGIZCTIVNLAgydhmrxwcjltpjdewxhxrtynyyuyhqwbpkwuqtpwmyhemjxvwoazumyfstoumreirdkwbmepwbrgmyhjgtqeltzxnwhbunvuoejnhfqcikggaqjgsoqhzrmu",
        "WOAECAAVWMSQMIMYMAPEVARGIZCTIVNLA"],
    [
        "RMPRWOBYTSjXGVJQPDQEHTWXMOGcHVWKATSWLBWPJBQTYKVHKMFKCYVVJXGLUEZTLSXChGBCAOAMiFEAPPAGWeMXXQAQTFCZGXKOGZLLUWTZDOYVWHIJZEIDOSHPwFWHYXCIZKTjKKVKQNDXMTCCBQMAGVCDPZOXHPSEQYthuqclzletakrqbzmaohadpog",
        "RMPRWOBYTSXGVJQPDQEHTWXMOGHVWKATSWLBWPJBQTYKVHKMFKCYVVJXGLUEZTLSXCGBCAOAMFEAPPAGWMXXQAQTFCZGXKOGZLLUWTZDOYVWHIJZEIDOSHPFWHYXCIZKTKKVKQNDXMTCCBQMAGVCDPZOXHPSEQY"]

]

A =   [
        "BFZZVHdQYHQEMNEFFRFJTQmNWHFVXRXlGTFNBqWQmyOWYWSTDSTMJRYHjBNTEWADLgHVgGIRGKFQSeCXNFNaIFAXOiQORUDROaNoJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMvSTGEQCYAJSFvbqivjuqvuzafvwwifnrlcxgbjmigkms",
        "BFZZVHQYHQEMNEFFRFJTQNWHFVXRXGTFNBWQOWYWSTDSTMJRYHBNTEWADLHVGIRGKFQSCXNFNIFAXOQORUDRONJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMSTGEQCYAJSF"]
# NO
# NO
# YES
# YES
# YES
# NO
# YES
# NO
# YES
# YES

# for l in L:
#     print(abbreviation(l[0], l[1]))

print(abbreviation(A[0], A[1]))