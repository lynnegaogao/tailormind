import { HuggingFaceQuestionAnswerConfig } from '../../types/huggingFace';
import { HuggingFaceQuestionAnswerResult } from '../../types/huggingFaceResult';
import { MessageContentI } from '../../types/messagesInternal';
import { HuggingFaceIO } from './huggingFaceIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class HuggingFaceQuestionAnswerIO extends HuggingFaceIO {
    permittedErrorPrefixes: string[];
    private readonly context;
    constructor(deepChat: DeepChat);
    preprocessBody(_: HuggingFaceQuestionAnswerConfig, messages: MessageContentI[]): {
        inputs: string;
    } | undefined;
    extractResultData(result: HuggingFaceQuestionAnswerResult): Promise<Response>;
}
//# sourceMappingURL=huggingFaceQuestionAnswerIO.d.ts.map