import { HuggingFaceClassificationResult } from '../../types/huggingFaceResult';
import { HuggingFaceFileIO } from './huggingFaceFileIO';
import { PollResult } from '../serviceIO';
import { DeepChat } from '../../deepChat';
export declare class HuggingFaceImageClassificationIO extends HuggingFaceFileIO {
    constructor(deepChat: DeepChat);
    extractPollResultData(result: HuggingFaceClassificationResult): PollResult;
}
//# sourceMappingURL=huggingFaceImageClassificationIO.d.ts.map