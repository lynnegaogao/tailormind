import { AzureTranslationResult } from '../../types/azureResult';
import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { DirectServiceIO } from '../utils/directServiceIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class AzureTranslationIO extends DirectServiceIO {
    insertKeyPlaceholderText: string;
    keyHelpUrl: string;
    url: string;
    constructor(deepChat: DeepChat);
    preprocessBody(messages: MessageContentI[]): {
        Text: string;
    }[] | undefined;
    callServiceAPI(messages: Messages, pMessages: MessageContentI[]): Promise<void>;
    extractResultData(result: AzureTranslationResult): Promise<Response>;
}
//# sourceMappingURL=azureTranslationIO.d.ts.map