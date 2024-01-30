import { HuggingFaceSummarizationResult } from '../../types/huggingFaceResult';
import { HuggingFaceIO } from './huggingFaceIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class HuggingFaceSummarizationIO extends HuggingFaceIO {
    constructor(deepChat: DeepChat);
    extractResultData(result: HuggingFaceSummarizationResult): Promise<Response>;
}
//# sourceMappingURL=huggingFaceSummarizationIO.d.ts.map