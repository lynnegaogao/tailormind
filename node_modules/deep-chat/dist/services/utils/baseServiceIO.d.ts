import { CameraFilesServiceConfig, MicrophoneFilesServiceConfig } from '../../types/fileServiceConfigs';
import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { ValidateInput } from '../../types/validateInput';
import { Demo as DemoT } from '../../types/demo';
import { Response } from '../../types/response';
import { Request } from '../../types/request';
import { DeepChat } from '../../deepChat';
import { KeyVerificationHandlers, CompletionsHandlers, ServiceFileTypes, RequestContents, StreamHandlers, ServiceIO } from '../serviceIO';
export declare class BaseServiceIO implements ServiceIO {
    readonly rawBody: any;
    deepChat: DeepChat;
    validateConfigKey: boolean;
    canSendMessage: ValidateInput;
    requestSettings: Request;
    fileTypes: ServiceFileTypes;
    camera?: CameraFilesServiceConfig;
    recordAudio?: MicrophoneFilesServiceConfig;
    totalMessagesMaxCharLength?: number;
    maxMessages?: number;
    demo?: DemoT;
    completionsHandlers: CompletionsHandlers;
    streamHandlers: StreamHandlers;
    constructor(deepChat: DeepChat, existingFileTypes?: ServiceFileTypes, demo?: DemoT);
    private static canSendMessage;
    verifyKey(_key: string, _keyVerificationHandlers: KeyVerificationHandlers): void;
    private static createCustomFormDataBody;
    private getServiceIOByType;
    private request;
    private callAPIWithText;
    private callApiWithFiles;
    callServiceAPI(messages: Messages, pMessages: MessageContentI[], files?: File[]): Promise<void>;
    callAPI(requestContents: RequestContents, messages: Messages): Promise<void>;
    extractResultData(result: any | Response): Promise<Response | {
        makingAnotherRequest: true;
    }>;
    isDirectConnection(): boolean;
    isWebModel(): boolean;
}
//# sourceMappingURL=baseServiceIO.d.ts.map