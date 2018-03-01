
.latestnewsenhanced_203.newslist {}

	.latestnewsenhanced_203 ul.newsitems {
		margin: 0;
		padding: 0;
		list-style: none;
		
		/* remove extra gaps between inline blocks */
	    font-size: 0;
	    letter-spacing: -1px; /* only for Safari */
	}
		
		@media only screen and (max-width: 480px) {
			.latestnewsenhanced_203 li.newsitem {
				width: 100% !important;
				margin-left: 0 !important;
				margin-right: 0 !important;
			}
		}
		
			
		.latestnewsenhanced_203 li.newsitem {
			width: 100%;
			overflow: hidden;
			display: inline-block;
			
							font-size: 14px;
					
			letter-spacing: normal;
			vertical-align: top;
			margin-bottom: 5px;
			margin-left: 0%;
			margin-right: 0%;
			list-style: none; /* To avoid possible template overrides */
		    padding: 0; /* To avoid possible template overrides */
		    background-image: none !important; /* To avoid possible template overrides */
		}
		
		.latestnewsenhanced_203 li.newsitem.active {
			background-color: #CCCCCC;
		}
		
			.latestnewsenhanced_203 .news {
				overflow: hidden;
				padding: 2px;
			}
			
			.latestnewsenhanced_203 .odd {
				border-bottom: none; /* to override k2 style */
				background: none; /* to override k2 style */
				padding: 0; /* to override k2 style */
			}
		
			.latestnewsenhanced_203 .even {
				border-bottom: none; /* to override k2 style */
				background: none; /* to override k2 style */
				padding: 0; /* to override k2 style */
			}
			
				.latestnewsenhanced_203 .newshead {		
					/* same column height fix */
					/* margin-bottom: -1000px;
					padding-bottom: 1000px;	*/	
				}
				
				.latestnewsenhanced_203 .headleft {
					float: left;
					margin-right: 8px;
				}
				
				.latestnewsenhanced_203 .headright {
					float: right;
					margin-left: 8px;
				}
				
					.latestnewsenhanced_203 .newshead .picture,
					.latestnewsenhanced_203 .newshead .nopicture,
					.latestnewsenhanced_203 .newshead .nodate {
						width: 0px;
						height: 0px;
						min-width: 0px;
						min-height: 0px;
					}
					
					.latestnewsenhanced_203 .newshead .calendar {
						width: 0px;
						min-width: 0px;						
					}
				
					.latestnewsenhanced_203 .newshead .calendar {
						/* next properties to avoid conflict with calendar.jos.css */
						border: none;
						font-family: inherit;
    					font-size: inherit;
					}	
					
					.latestnewsenhanced_203 .newshead .calendar.noimage {			
						background: #F4F4F4; /* Old browsers */
						background: -moz-linear-gradient(top, #ffffff 0%, #e5e5e5 100%); /* FF3.6+ */
						background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#ffffff), color-stop(100%,#e5e5e5)); /* Chrome,Safari4+ */
						background: -webkit-linear-gradient(top, #ffffff 0%,#e5e5e5 100%); /* Chrome10+,Safari5.1+ */
						background: -o-linear-gradient(top, #ffffff 0%,#e5e5e5 100%); /* Opera11.10+ */
						background: -ms-linear-gradient(top, #ffffff 0%,#e5e5e5 100%); /* IE10+ */
						filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#e5e5e5',GradientType=0 ); /* IE6-9 */
						background: linear-gradient(top, #ffffff 0%,#e5e5e5 100%); /* W3C */
						
						color: #3D3D3D;						
						
						border-radius: 4px;
						-moz-border-radius: 4px;
						-webkit-border-radius: 4px;
						/* IE 7 AND 8 DO NOT SUPPORT BORDER RADIUS */
						
						-moz-background-clip: padding-box;
						-webkit-background-clip: padding-box;
						background-clip: padding-box;
						/* Use "background-clip: padding-box" when using rounded corners to avoid the gradient bleeding through the corners */
						
						border: 1px solid #DDDDDD;
					}		
		
						.latestnewsenhanced_203 .newshead .calendar .weekday, 
						.latestnewsenhanced_203 .newshead .calendar .month, 
						.latestnewsenhanced_203 .newshead .calendar .day, 
						.latestnewsenhanced_203 .newshead .calendar .year,
						.latestnewsenhanced_203 .newshead .calendar .time {
							position: relative;
							width: 100%;
							text-align: center;
						}
						
						.latestnewsenhanced_203 .newshead .calendar.noimage .weekday {							
							background: #C8C8C8; /* Old browsers */
							background: -moz-linear-gradient(top, #eeeeee 0%, #cccccc 100%); /* FF3.6+ */
							background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#eeeeee), color-stop(100%,#cccccc)); /* Chrome,Safari4+ */
							background: -webkit-linear-gradient(top, #eeeeee 0%,#cccccc 100%); /* Chrome10+,Safari5.1+ */
							background: -o-linear-gradient(top, #eeeeee 0%,#cccccc 100%); /* Opera11.10+ */
							background: -ms-linear-gradient(top, #eeeeee 0%,#cccccc 100%); /* IE10+ */
							filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#eeeeee', endColorstr='#cccccc',GradientType=0 ); /* IE6-9 */
							background: linear-gradient(top, #eeeeee 0%,#cccccc 100%); /* W3C */						
							
							color: #494949;						
							
							border-top-right-radius: 4px;
							border-top-left-radius: 4px;
							-moz-border-top-right-radius: 4px;
							-moz-border-top-left-radius: 4px;
							-webkit-border-top-right-radius: 4px;
							-webkit-border-top-left-radius: 4px;
							
							-moz-background-clip: padding-box;
							-webkit-background-clip: padding-box;
							background-clip: padding-box;
							/* Use "background-clip: padding-box" when using rounded corners to avoid the gradient bleeding through the corners */		
						}
						
						.latestnewsenhanced_203 .newshead .calendar.noimage .time {							
							background: #C8C8C8; /* Old browsers */
							background: -moz-linear-gradient(top, #cccccc 0%, #eeeeee 100%); /* FF3.6+ */
							background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#cccccc), color-stop(100%,#eeeeee)); /* Chrome,Safari4+ */
							background: -webkit-linear-gradient(top, #cccccc 0%,#eeeeee 100%); /* Chrome10+,Safari5.1+ */
							background: -o-linear-gradient(top, #cccccc 0%,#eeeeee 100%); /* Opera11.10+ */
							background: -ms-linear-gradient(top, #cccccc 0%,#eeeeee 100%); /* IE10+ */
							filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#cccccc', endColorstr='#eeeeee',GradientType=0 ); /* IE6-9 */
							background: linear-gradient(top, #cccccc 0%,#eeeeee 100%); /* W3C */						
							
							color: #494949;						
							
							border-bottom-right-radius: 4px;
							border-bottom-left-radius: 4px;
							-moz-border-bottom-right-radius: 4px;
							-moz-border-bottom-left-radius: 4px;
							-webkit-border-bottom-right-radius: 4px;
							-webkit-border-bottom-left-radius: 4px;
							
							-moz-background-clip: padding-box;
							-webkit-background-clip: padding-box;
							background-clip: padding-box;
							/* Use "background-clip: padding-box" when using rounded corners to avoid the gradient bleeding through the corners */		
							
						}
				
						.latestnewsenhanced_203 .newshead .calendar .weekday {
							font-size: 1em;
							text-transform: uppercase;
							letter-spacing: 0.4em;
							line-height: 1.5em;
						}
						
						.latestnewsenhanced_203 .newshead .calendar .month {
							font-size: 0.8em;
							font-weight: bold;
							letter-spacing: 0.45em;
							line-height: 1.2em;
							margin-top: 0.2em;
							margin-bottom: 0.2em;
						}
						
						.latestnewsenhanced_203 .newshead .calendar .day {	
							font-size: 2em;
							font-weight: bold;
							letter-spacing: 0.1em;
							line-height: 0.8em;  
							margin-bottom: 0.2em;  						
						}
						
						.latestnewsenhanced_203 .newshead .calendar .year {
							font-size: 0.8em;
							letter-spacing: 0.35em;
							line-height: 1.2em;
							margin-bottom: 0.2em;
						}
						
						.latestnewsenhanced_203 .newshead .calendar .time {
							font-size: 0.8em;
							letter-spacing: 0.1em;
							line-height: 1.7em;
						}				
	
					.latestnewsenhanced_203 .newshead .picture {
		    			overflow: hidden;
						background-color: #FFFFFF;
						border: 1px solid #CCCCCC;
						padding: 3px;
						text-align: center;
					}
					
					.latestnewsenhanced_203 .newshead .picture a,
					.latestnewsenhanced_203 .newshead .nopicture a {
						text-decoration: none;
						display: inline-block;
						height: 100%;
	    				width: 100%;
	    				cursor: hand;
					}
					
					.latestnewsenhanced_203 .newshead .picture a:hover,
					.latestnewsenhanced_203 .newshead .nopicture a:hover {
						text-decoration: none;
					}
		
					.latestnewsenhanced_203  .newshead .picture img {
						max-width: 100%;
						max-height: 100%;
					}
					
					.latestnewsenhanced_203 .newshead .picture .defaultpicture {}
					
					.latestnewsenhanced_203 .newshead .nopicture {
		    			overflow: hidden;
						background-color: #FFFFFF;
						border: 1px solid #CCCCCC;
						padding: 3px;
						text-align: center;
					}
		
					.latestnewsenhanced_203 .newshead .nopicture span {
						background-color: #F4F4F4;
						display: inline-block;
						width: 100%;
						height: 100%;
					}
	
				.latestnewsenhanced_203 .newsinfo {
											overflow: hidden;
									}
				
				.latestnewsenhanced_203 .infonoimageleft {}	
						
				.latestnewsenhanced_203 .infoleft {
					/*clear: right;
					margin-left: 8px;*/
				}
				
				.latestnewsenhanced_203 .infonoimageright {
					text-align: right;
				}
				
				.latestnewsenhanced_203 .inforight {
					/*clear: left; */
					text-align: right;
					/*margin-right: 8px;*/
				}
				
					.latestnewsenhanced_203 .newstitle {
						margin: 0;
					}
					
										
					.latestnewsenhanced_203 .newsintro {
					}
					
					.latestnewsenhanced_203 .newsextra {
						font-size: 0.8em;
					}
					
						.latestnewsenhanced_203 .newsextra .delimiter {
							padding: 0 3px;
						}
					
						.latestnewsenhanced_203 .newsextra .delimiter:before {
							content: "-";
						}
				
					.latestnewsenhanced_203 .link {}
					
					.latestnewsenhanced_203 .catlink {}

	.latestnewsenhanced_203 .pagination {
		margin: 0;
		padding: 0;
		list-style: none;
		text-align: center;
		position: relative;
		clear: both;
	}
	
	.latestnewsenhanced_203 .pagination li {
		display: inline;
		list-style: none;
		cursor: pointer;
	}
	
	.latestnewsenhanced_203 .pagination li.active span {
		text-decoration: underline;
	}
	
	.latestnewsenhanced_203 .pagination li.disabled span {
		color: #999999;
		cursor: default;
	}
	
	.latestnewsenhanced_203 .onecatlink {
		margin-right: 0%;
		text-align: right;
	}		
	
	.latestnewsenhanced_203 .error-message {
		width: 100%;
	}
	
	.latestnewsenhanced_203 .error-message dl {
		border: 1px solid #EED3D7;
		border-radius: 4px;
		background-color: #F2DEDE;
		color: #B94A48;
	}
	
	.latestnewsenhanced_203 .error-message dt {
		border-bottom: 1px solid #EED3D7;
		padding-left: 5px;
	}
	
	.latestnewsenhanced_203 .error-message dd {
		word-wrap: break-word;
		margin-bottom: 3px;
    	margin-top: 3px;
    	margin-left: 5px;
	}
		