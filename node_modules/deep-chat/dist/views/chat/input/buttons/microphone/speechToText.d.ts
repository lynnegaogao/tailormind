import { TextInputEl } from '../../textInput/textInput';
import { Messages } from '../../../messages/messages';
import { MicrophoneButton } from './microphoneButton';
import { DeepChat } from '../../../../../deepChat';
export type AddErrorMessage = Messages['addNewErrorMessage'];
export declare class SpeechToText extends MicrophoneButton {
    private readonly _addErrorMessage;
    constructor(deepChat: DeepChat, textInput: TextInputEl, addErrorMessage: AddErrorMessage);
    private static processConfiguration;
    private static getServiceName;
    private buttonClick;
    private onCommandModeTrigger;
    private onError;
}
//# sourceMappingURL=speechToText.d.ts.map