from emotion_detection import emotion_detector
import unittest

class TestEmotion(unittest.TestCase):
    def test_emotion(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['Dominant_Emotion'], 'Joy')
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['Dominant_Emotion'], 'Anger')
        result_3 = emotion_detector('I feel disgusted just hearing about thi')
        self.assertEqual(result_3['Dominant_Emotion'], 'Disgust')        
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['Dominant_Emotion'], 'Sadness')
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['Dominant_Emotion'], 'Fear')



unittest.main()