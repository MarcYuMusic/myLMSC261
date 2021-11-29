### Marc's GitHub Troll

This is the project that I've been watching, and also what I'l be using for my final project: https://github.com/ageitgey/face_recognition. There weren't any recent changes and all of the notifications I received over the past two weeks were issues people had with the program. The last updates to the program were more than 4 years ago. I'm going to instead pick out some of the issues that had responses to them.

3 or more changes that happened to the program that you found interesting:
- A few people had an issue with something called "dlib" using CPU instead of GPU. (https://github.com/ageitgey/face_recognition/issues/1375)
- Someone was unable to get the program working in Linux. (https://github.com/ageitgey/face_recognition/issues/1368)
- Someone had a bunch of misidientifications where the program was misidentifying people. (https://github.com/ageitgey/face_recognition/issues/1339)

What you thought of how those changes were described in comments:
- When describing their problems, people often listed their operating system and program version as well. People would also list specs of their computer and copy and paste code. Having a clear description (or markdown file) is super important to understand where the error might've happened.

What you thought of how the collaborators communicated on the platform:
- If the specs weren't enough to solve the problem, people would ask further questions. For example, "Did you compile dlib from source?". And someone else with the same issue replied, "Same issue here. I did compile DLIB (19.22) from source and checked the CMAKE output for indication that DLIB will use CUDA. According to jtop, GPU is not being used." Like I mentioned above, I think these were good examples to show how important having a clear markdown is for any program.