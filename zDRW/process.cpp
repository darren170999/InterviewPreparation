#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

void processFiles(const std::string& basePath, const std::string& fillPath, const std::string& removePath, const std::string& outputPath) {
    // Read fill_file
    std::ifstream fillFile(fillPath);
    std::string fillLine;
    std::getline(fillFile, fillLine);
    fillFile.close();

    // Remove newline characters and trailing whitespace from fillLine
    fillLine.erase(std::remove(fillLine.begin(), fillLine.end(), '\r'), fillLine.end());
    fillLine.erase(std::remove(fillLine.begin(), fillLine.end(), '\n'), fillLine.end());
    fillLine.erase(std::remove_if(fillLine.begin(), fillLine.end(), ::isspace), fillLine.end());

    // Read remove_file
    std::ifstream removeFile(removePath);
    std::string removeLine;
    if (std::getline(removeFile, removeLine)) {
        // Remove newline characters and trailing whitespace from removeLine
        removeLine.erase(std::remove(removeLine.begin(), removeLine.end(), '\r'), removeLine.end());
        removeLine.erase(std::remove(removeLine.begin(), removeLine.end(), '\n'), removeLine.end());
        removeLine.erase(std::remove_if(removeLine.begin(), removeLine.end(), ::isspace), removeLine.end());
    }
    removeFile.close();

    // Process base_file
    std::ifstream baseFile(basePath);
    std::vector<std::string> baseLines;
    std::string line;
    while (std::getline(baseFile, line)) {
        baseLines.push_back(line);
    }
    baseFile.close();

    std::vector<std::string> modifiedLines;
    int emptyLineCount = 0;

    for (const std::string& origLine : baseLines) {
        std::string line = origLine;
        
        if (line.empty()) {
            emptyLineCount++;
            line = fillLine;
        } else if (!removeLine.empty()) {
            size_t pos = line.find(removeLine);
            while (pos != std::string::npos) {
                line.replace(pos, removeLine.length(), "");
                pos = line.find(removeLine, pos);
            }
        }
        
        modifiedLines.push_back(line);
    }

    // Write the modifications to output_file
    std::ofstream outputFile(outputPath);
    outputFile << "There are " << modifiedLines.size() << " lines in base file." << std::endl;
    outputFile << "There are " << emptyLineCount << " empty lines in base file." << std::endl;
    for (const std::string& modifiedLine : modifiedLines) {
        outputFile << modifiedLine << std::endl;
    }
    outputFile.close();
}

int main() {
    std::string basePath = "path_to_base_file.txt";
    std::string fillPath = "path_to_fill_file.txt";
    std::string removePath = "path_to_remove_file.txt";
    std::string outputPath = "path_to_output_file.txt";

    processFiles(basePath, fillPath, removePath, outputPath);

    return 0;
}