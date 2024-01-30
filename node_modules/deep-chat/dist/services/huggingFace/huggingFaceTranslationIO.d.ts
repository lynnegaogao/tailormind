import { HuggingFaceTranslationResult } from '../../types/huggingFaceResult';
import { HuggingFaceIO } from './huggingFaceIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class HuggingFaceTranslationIO extends HuggingFaceIO {
    constructor(deepChat: DeepChat);
    extractResultData(result: HuggingFaceTranslationResult): Promise<Response>;
}
//# sourceMappingURL=huggingFaceTranslationIO.d.ts.map