import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { CohereChatResult } from '../../types/cohereResult';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
import { CohereIO } from './cohereIO';
export declare class CohereChatIO extends CohereIO {
    constructor(deepChat: DeepChat);
    private preprocessBody;
    callServiceAPI(messages: Messages, pMessages: MessageContentI[]): Promise<void>;
    extractResultData(result: CohereChatResult): Promise<Response>;
}
//# sourceMappingURL=cohereChatIO.d.ts.map