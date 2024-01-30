import { AzureSpeechToTextResult } from '../../types/azureResult';
import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { AzureSpeechIO } from './azureSpeechIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class AzureSpeechToTextIO extends AzureSpeechIO {
    private static readonly HELP_LINK;
    introPanelMarkUp: string;
    url: string;
    isTextInputDisabled: boolean;
    textInputPlaceholderText: string;
    constructor(deepChat: DeepChat);
    private static canFileSendMessage;
    callServiceAPI(messages: Messages, _: MessageContentI[], files?: File[]): Promise<void>;
    extractResultData(result: AzureSpeechToTextResult): Promise<Response>;
}
//# sourceMappingURL=azureSpeechToTextIO.d.ts.map