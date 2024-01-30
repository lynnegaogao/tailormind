import { WebModelIntro } from '../types/webModel/webModel';
export declare class WebModelIntroMessage {
    private static readonly DOWNLOAD_BUTTON_CLASS;
    private static readonly UPLOAD_BUTTON_CLASS;
    private static readonly FILE_INPUT_CLASS;
    private static readonly EXPORT_BUTTON_CLASS;
    private static enableButtons;
    static setUpInitial(init: (files?: FileList) => void, introMessage?: WebModelIntro, chatEl?: HTMLElement, isWorker?: boolean): string;
    private static exportFile;
    static setUpAfterLoad(files: File[], introMessage?: WebModelIntro, chatEl?: HTMLElement, isWorker?: boolean): string;
}
//# sourceMappingURL=webModelIntroMessage.d.ts.map