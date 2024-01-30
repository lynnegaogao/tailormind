type AssignNever<T, K> = K & {
    [B in Exclude<keyof T, keyof K>]?: never;
};
type BuildUniqueInterfaces<CompleteInterface, Interfaces> = Interfaces extends object ? AssignNever<CompleteInterface, Interfaces> : never;
type UnionToIntersection<U> = (U extends unknown ? (k: U) => void : never) extends (k: infer I) => void ? I : never;
export type InterfacesUnion<Interfaces> = BuildUniqueInterfaces<UnionToIntersection<Interfaces>, Interfaces>;
export type OverrideTypes<T, U> = {
    [P in keyof T]: U;
};
export type PropsRequired<T, K extends keyof T> = T & {
    [P in K]-?: T[P];
};
export {};
//# sourceMappingURL=utilityTypes.d.ts.map