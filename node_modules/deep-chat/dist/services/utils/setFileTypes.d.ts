import { ServiceFileTypes, ServiceIO } from '../serviceIO';
import { DeepChat } from '../../deepChat';
export declare class SetFileTypes {
    private static parseConfig;
    private static processMixedFiles;
    private static processMicrophone;
    private static processAudioConfig;
    private static processGifConfig;
    private static processCamera;
    private static processImagesConfig;
    private static populateDefaultFileIO;
    static set(deepChat: DeepChat, serviceIO: ServiceIO, existingFileTypes?: ServiceFileTypes): void;
}
//# sourceMappingURL=setFileTypes.d.ts.map