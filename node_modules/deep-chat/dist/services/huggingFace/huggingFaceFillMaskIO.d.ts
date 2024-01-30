import { HuggingFaceFillMaskResult } from '../../types/huggingFaceResult';
import { HuggingFaceIO } from './huggingFaceIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class HuggingFaceFillMaskIO extends HuggingFaceIO {
    introPanelMarkUp: string;
    permittedErrorPrefixes: string[];
    constructor(deepChat: DeepChat);
    extractResultData(result: HuggingFaceFillMaskResult): Promise<Response>;
}
//# sourceMappingURL=huggingFaceFillMaskIO.d.ts.map