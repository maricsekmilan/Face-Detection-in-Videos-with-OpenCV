## Face Detection in Videos with OpenCV


<table style="border: none;">
  <tr>
    <td style="padding-right: 10px; border: none;">
      <img src="https://github.com/user-attachments/assets/cd3853a9-3d91-406d-b388-2055b3957d55" alt="video2-ezgif com-video-to-gif-converter">
    </td>
    <td style="border: none;">
      <img src="https://github.com/user-attachments/assets/1841fb46-044d-4973-a4f5-0d06c846c7e0" alt="output2-ezgif com-video-to-gif-converter">
    </td>
  </tr>
</table>

## Libraries Used
This project is implemented in Python and relies on the following libraries:
- `cv2` (OpenCV): For video reading, face detection, and video writing.
- `sys`: For terminal-based progress updates.

Ensure you have OpenCV installed before running the script. You can install it via pip:
```bash
pip install opencv-python
```

## License Information
This project uses a pre-trained Haar Cascade Classifier file (`faces.xml`) provided by OpenCV. The classifier file is licensed under the **Intel License Agreement for the Open Source Computer Vision Library**. Key points include:
- The file may be redistributed and modified, provided the original license text is retained.
- Redistribution in binary form must include the license in associated documentation.
- The software is provided "as is" without any warranty.

For more details, refer to the full license text included in the `faces.xml` file.

## How to Use
1. Place the Haar Cascade XML file (`faces.xml`) in the same directory as the script.
2. Update the script to specify the input video file path (`*ORIGINAL_VIDEO_NAME*.mp4` in the script).
3. Run the script:
   ```bash
   python face_detection.py
   ```
4. The processed video with face annotations will be saved as `*OUTPUT_VIDEO_NAME*.avi` in the same directory.
5. Monitor the progress in the terminal, displayed as a percentage of frames processed.

## Applications
This project can be used as a starting point for various applications, such as:
- Automated video surveillance.
- Preprocessing video data for machine learning tasks.
- Face detection for video editing or content analysis.
