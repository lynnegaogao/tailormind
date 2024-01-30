import { CohereSummarizationConfig } from '../../types/cohere';
import { CohereSummarizationResult } from '../../types/cohereResult';
import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
import { CohereIO } from './cohereIO';
export declare class CohereSummarizationIO extends CohereIO {
    constructor(deepChat: DeepChat);
    preprocessBody(body: CohereSummarizationConfig, messages: MessageContentI[]): any;
    callServiceAPI(messages: Messages, pMessages: MessageContentI[]): Promise<void>;
    extractResultData(result: CohereSummarizationResult): Promise<Response>;
}
//# sourceMappingURL=cohereSummarizationIO.d.ts.map