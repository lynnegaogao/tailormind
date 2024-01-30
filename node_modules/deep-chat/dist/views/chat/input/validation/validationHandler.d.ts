import { FileAttachments } from '../fileAttachments/fileAttachments';
import { SubmitButton } from '../buttons/submit/submitButton';
import { ServiceIO } from '../../../../services/serviceIO';
import { TextInputEl } from '../textInput/textInput';
import { DeepChat } from '../../../../deepChat';
export declare class ValidationHandler {
    private static validate;
    private static useValidationFunc;
    private static useValidationFuncProgrammatic;
    private static validateWebsocket;
    static attach(deepChat: DeepChat, serviceIO: ServiceIO, textInput: TextInputEl, fileAttachments: FileAttachments, submitButton: SubmitButton): void;
}
//# sourceMappingURL=validationHandler.d.ts.map