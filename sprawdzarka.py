import os, glob, filecmp

executableName = "executable.exe"
testsPath = "tests/"
output = testsPath+"output.out"
testCaseNumber = 0

successfulTests = 0
successRatio = 0.0

for testCase in glob.glob(testsPath+"*.in"):
    testCaseNumber = testCaseNumber+1
    expectedOutput = os.path.splitext(testCase)[0]+".out"
    os.system(executableName +" < " + testCase + " > " + output);
    success = filecmp.cmp(expectedOutput, output) 
    if success == True:
        successMessage = "YEAH, TEST CASE #" + str(testCaseNumber) + " PASSED!!!"   
        print(successMessage)
        successfulTests = successfulTests+1
    else:
        errorMessage = "OH NO, TEST CASE #" + str(testCaseNumber) + " FAILED!!!"
        print(errorMessage)
successRatio = successfulTests/testCaseNumber * 100.0
print("RESULT - " + str(successfulTests)+"/"+str(testCaseNumber)+"("+str(successRatio)+"%)")
