//
//  AGCKAPIManager.h
//
//  Created by JohnnyB0Y on 2018/11/14.
//  Copyright © 2018年 JohnnyB0Y. All rights reserved.
//

#import <CTAPIBaseManager.h>
#import "CTAPIBaseManager+WNAPIBaseManager.h"

@interface AGCKAPIManager () CTAPIBaseManager
<CTAPIManager, CTAPIManagerValidator, CTPagableAPIManager>

@property (nonatomic, assign) NSInteger pageSize;
@property (nonatomic, assign, readonly) NSUInteger currentPageNumber;
@property (nonatomic, assign, readonly) BOOL isLastPage;


- (void)loadNextPage;

@end
