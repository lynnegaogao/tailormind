import { HuggingFaceAudioRecognitionResult } from '../../types/huggingFaceResult';
import { HuggingFaceFileIO } from './huggingFaceFileIO';
import { PollResult } from '../serviceIO';
import { DeepChat } from '../../deepChat';
export declare class HuggingFaceAudioRecognitionIO extends HuggingFaceFileIO {
    constructor(deepChat: DeepChat);
    extractPollResultData(result: HuggingFaceAudioRecognitionResult): PollResult;
}
//# sourceMappingURL=huggingFaceAudioRecognitionIO.d.ts.map