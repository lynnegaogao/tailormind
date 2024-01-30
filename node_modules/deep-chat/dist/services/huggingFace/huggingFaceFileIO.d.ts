import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { HuggingFaceModel } from '../../types/huggingFace';
import { ServiceFileTypes } from '../serviceIO';
import { HuggingFaceIO } from './huggingFaceIO';
import { APIKey } from '../../types/APIKey';
import { DeepChat } from '../../deepChat';
export declare class HuggingFaceFileIO extends HuggingFaceIO {
    isTextInputDisabled: boolean;
    constructor(deepChat: DeepChat, placeholderText: string, defaultModel: string, config: true | (HuggingFaceModel), apiKey?: APIKey, existingFileTypes?: ServiceFileTypes);
    private static canSendFile;
    preprocessBody(_: {}, __: MessageContentI[], files: File[]): {
        inputs: string;
    };
    callServiceAPI(messages: Messages, _: MessageContentI[], files?: File[]): Promise<void>;
}
//# sourceMappingURL=huggingFaceFileIO.d.ts.map