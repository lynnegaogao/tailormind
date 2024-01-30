import { HuggingFaceTextGenerationResult } from '../../types/huggingFaceResult';
import { HuggingFaceIO } from './huggingFaceIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class HuggingFaceTextGenerationIO extends HuggingFaceIO {
    constructor(deepChat: DeepChat);
    extractResultData(result: HuggingFaceTextGenerationResult): Promise<Response>;
}
//# sourceMappingURL=huggingFaceTextGenerationIO.d.ts.map