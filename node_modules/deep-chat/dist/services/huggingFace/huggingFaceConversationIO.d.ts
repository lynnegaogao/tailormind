import { HuggingFaceConversationResult } from '../../types/huggingFaceResult';
import { HuggingFaceQuestionAnswerConfig } from '../../types/huggingFace';
import { MessageContentI } from '../../types/messagesInternal';
import { HuggingFaceIO } from './huggingFaceIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class HuggingFaceConversationIO extends HuggingFaceIO {
    constructor(deepChat: DeepChat);
    private processMessages;
    preprocessBody(body: HuggingFaceQuestionAnswerConfig, messages: MessageContentI[]): {
        inputs: string;
    } | undefined;
    extractResultData(result: HuggingFaceConversationResult): Promise<Response>;
}
//# sourceMappingURL=huggingFaceConversationIO.d.ts.map