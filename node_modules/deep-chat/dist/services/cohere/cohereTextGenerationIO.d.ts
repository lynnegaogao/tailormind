import { CohereCompletionsResult } from '../../types/cohereResult';
import { CohereGenerateConfig } from '../../types/cohere';
import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
import { CohereIO } from './cohereIO';
export declare class CohereTextGenerationIO extends CohereIO {
    constructor(deepChat: DeepChat);
    preprocessBody(body: CohereGenerateConfig, messages: MessageContentI[]): any;
    callServiceAPI(messages: Messages, pMessages: MessageContentI[]): Promise<void>;
    extractResultData(result: CohereCompletionsResult): Promise<Response>;
}
//# sourceMappingURL=cohereTextGenerationIO.d.ts.map