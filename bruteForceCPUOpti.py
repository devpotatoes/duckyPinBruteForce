def generateDuckyScript(pinLength, numpadGridObj, delaysTuple, outputPath, debugPinTestRange = 0):
    open(outputPath, "w").close()

    moveDelay = delaysTuple[0]
    clickDelay = delaysTuple[1]
    
    initPosX, initPosY = numpadGridObj["1"]
    currentPosX, currentPosY = initPosX, initPosY
    
    pinPossibilities = 10 ** pinLength

    if debugPinTestRange > 0:
        pinPossibilities = debugPinTestRange

    duckyScriptLinesArray = []

    for pin in range(pinPossibilities):
        duckyScriptLinesArray.append(f"DELAY {moveDelay}")

        for digit in str(pin).zfill(pinLength):
            targetPosX, targetPosY = numpadGridObj[digit]

            totalTranslateX = targetPosX - currentPosX
            totalTranslateY = targetPosY - currentPosY

            while totalTranslateX != 0:
                translateX = min(128, abs(totalTranslateX)) * (1 if (totalTranslateX > 0) else -1)

                duckyScriptLinesArray.append(f"MOUSEMOVE {translateX} 0")
                duckyScriptLinesArray.append(f"DELAY {moveDelay}")
                
                totalTranslateX -= translateX
                currentPosX += translateX

            while totalTranslateY != 0:
                translateY = min(128, abs(totalTranslateY)) * (1 if (totalTranslateY > 0) else -1)

                duckyScriptLinesArray.append(f"MOUSEMOVE 0 {translateY}")
                duckyScriptLinesArray.append(f"DELAY {moveDelay}")
                
                totalTranslateY -= translateY
                currentPosY += translateY

            duckyScriptLinesArray.append("LEFTCLICK")
            duckyScriptLinesArray.append(f"DELAY {clickDelay}")

    with open(outputPath, "a") as file:
        file.write("\n".join(duckyScriptLinesArray) + "\n")

    print(f"Process successfully completed, your DuckyScript is available !\nOutput: \"{outputPath}\"")